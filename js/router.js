// ============================================
// FILE: js/router.js
// ============================================

const Router = {
    routes: {},
    currentRoute: null,
    
    // Đăng ký route
    register(name, handler) {
        this.routes[name] = handler;
    },
    
    // Điều hướng đến route
    navigate(route, params = {}) {
        // Lưu route hiện tại
        this.currentRoute = { route, params };
        
        // Cập nhật URL hash
        const hashParams = Object.entries(params)
            .map(([key, value]) => `${key}=${value}`)
            .join('&');
        window.location.hash = route + (hashParams ? '?' + hashParams : '');
        
        // Gọi handler
        if (this.routes[route]) {
            this.routes[route](params);
        } else {
            console.error(`Route not found: ${route}`);
            this.navigate('home');
        }
        
        // Cập nhật active state cho nav
        this.updateActiveNav(route, params);
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    
    // Parse URL hash
    parseHash() {
        const hash = window.location.hash.slice(1);
        if (!hash) return { route: 'home', params: {} };
        
        const [route, queryString] = hash.split('?');
        const params = {};
        
        if (queryString) {
            queryString.split('&').forEach(param => {
                const [key, value] = param.split('=');
                params[key] = decodeURIComponent(value);
            });
        }
        
        return { route: route || 'home', params };
    },
    
    // Cập nhật active state cho navigation
    updateActiveNav(route, params) {
        // Remove all active classes
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        
        // Add active class to current route
        const selector = `[data-route="${route}"]`;
        const navLink = document.querySelector(selector);
        if (navLink) {
            navLink.closest('.nav-link')?.classList.add('active');
        }
    },
    
    // Khởi tạo router
    init() {
        // Handle browser back/forward
        window.addEventListener('hashchange', () => {
            const { route, params } = this.parseHash();
            this.navigate(route, params);
        });
        
        // Handle initial load
        const { route, params } = this.parseHash();
        this.navigate(route, params);
        
        // Setup click handlers for all links with data-route
        document.addEventListener('click', (e) => {
            const link = e.target.closest('[data-route]');
            if (link) {
                e.preventDefault();
                const route = link.dataset.route;
                const params = {};
                
                // Collect all data attributes as params
                Object.keys(link.dataset).forEach(key => {
                    if (key !== 'route') {
                        params[key] = link.dataset[key];
                    }
                });
                
                this.navigate(route, params);
            }
        });
    }
};
