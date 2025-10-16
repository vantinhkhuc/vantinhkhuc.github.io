// ============================================
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
            script.on
