/ ============================================
// FILE: js/app.js
// ============================================

const App = {
    // Cấu hình
    config: {
        dataPath: 'data',
        enableCache: true,
        cacheTimeout: 300000 // 5 minutes
    },
    
    // Cache
    cache: new Map(),
    
    // Modules
    modules: {},
    
    // Khởi tạo ứng dụng
    async init() {
        console.log('🚀 Initializing App...');
        
        // Register routes
        this.registerRoutes();
        
        // Initialize router
        Router.init();
        
        // Load modules dynamically
        await this.loadModules();
        
        console.log('✅ App initialized successfully');
    },
    
    // Đăng ký routes
    registerRoutes() {
        Router.register('home', () => this.showHome());
        Router.register('news', (params) => this.loadModule('news', params));
        Router.register('finance', (params) => this.loadModule('finance', params));
        Router.register('blog', (params) => this.loadModule('blog', params));
    },
    
    // Hiển thị trang chủ
    showHome() {
        document.getElementById('homePage').classList.remove('hidden');
        document.getElementById('dynamicContent').classList.add('hidden');
        document.getElementById('dynamicContent').innerHTML = '';
    },
    
    // Load module
    async loadModule(moduleName, params) {
        // Hide home page
        document.getElementById('homePage').classList.add('hidden');
        const container = document.getElementById('dynamicContent');
        container.classList.remove('hidden');
        
        // Show loading
        this.showLoading(container);
        
        try {
            // Check if module is loaded
            if (!this.modules[moduleName]) {
                await this.loadModuleScript(moduleName);
            }
            
            // Initialize module
            if (this.modules[moduleName] && this.modules[moduleName].init) {
                await this.modules[moduleName].init(params, container);
            } else {
                throw new Error(`Module ${moduleName} not found or invalid`);
            }
        } catch (error) {
            console.error(`Error loading module ${moduleName}:`, error);
            this.showError(container, error.message);
        }
    },
    
    // Load module script dynamically
    async loadModuleScript(moduleName) {
        return new Promise((resolve, reject) => {
            // Check if already loaded
            if (window[`${moduleName}Module`]) {
                this.modules[moduleName] = window[`${moduleName}Module`];
                resolve();
                return;
            }
            
            // Load script
            const script = document.createElement('script');
            script.src = `js/modules/${moduleName}.js`;
            script.onload = () => {
                this.modules[moduleName] = window[`${moduleName}Module`];
                console.log(`✅ Module ${moduleName} loaded`);
                resolve();
            };
            script.onerror = () => {
                reject(new Error(`Failed to load module: ${moduleName}`));
            };
            document.head.appendChild(script);
        });
    },
    
    // Tải dữ liệu từ JSON
    async loadData(path) {
        // Check cache
        if (this.config.enableCache && this.cache.has(path)) {
            const cached = this.cache.get(path);
            const now = Date.now();
            
            if (now - cached.timestamp < this.config.cacheTimeout) {
                console.log(`📦 Using cached data: ${path}`);
                return cached.data;
            }
        }
        
        // Fetch data
        try {
            console.log(`🔄 Fetching data: ${path}`);
            const response = await fetch(`${this.config.dataPath}/${path}`);
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const data = await response.json();
            
            // Cache data
            if (this.config.enableCache) {
                this.cache.set(path, {
                    data: data,
                    timestamp: Date.now()
                });
            }
            
            return data;
        } catch (error) {
            console.error(`Error loading data from ${path}:`, error);
            throw error;
        }
    },
    
    // Clear cache
    clearCache() {
        this.cache.clear();
        console.log('🗑️ Cache cleared');
    },
    
    // Show loading state
    showLoading(container) {
        container.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <div class="loading-text">Đang tải dữ liệu...</div>
            </div>
        `;
    },
    
    // Show error state
    showError(container, message) {
        container.innerHTML = `
            <div class="error-message">
                <h3>⚠️ Đã Xảy Ra Lỗi</h3>
                <p>${message}</p>
                <p style="margin-top: 10px;">
                    <button onclick="location.reload()" style="padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer;">
                        Thử lại
                    </button>
                    <button onclick="Router.navigate('home')" style="padding: 10px 20px; background: #ccc; color: #333; border: none; border-radius: 5px; cursor: pointer; margin-left: 10px;">
                        Về trang chủ
                    </button>
                </p>
            </div>
        `;
    },
    
    // Utility: Format number
    formatNumber(num, decimals = 2) {
        return num.toLocaleString('vi-VN', {
            minimumFractionDigits: decimals,
            maximumFractionDigits: decimals
        });
    },
    
    // Utility: Format date
    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('vi-VN', {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit'
        });
    },
    
    // Utility: Format currency
    formatCurrency(amount, currency = 'VND') {
        return new Intl.NumberFormat('vi-VN', {
            style: 'currency',
            currency: currency
        }).format(amount);
    },
    
    // Utility: Truncate text
    truncateText(text, maxLength = 100) {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    }
};
