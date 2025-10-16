// ============================================
// FILE: js/modules/blog.js (Template)
// ============================================

window.blogModule = {
    name: 'blog',
    data: null,
    
    async init(params, container) {
        console.log('✍️ Loading Blog Module...', params);
        
        const page = params.page || 'profile';
        
        try {
            this.data = await App.loadData(`blog/${page}.json`);
            this.render(container, page);
        } catch (error) {
            console.warn('Using sample data for blog');
            this.renderSampleData(container, page);
        }
    },
    
    render(container, page) {
        const pageNames = {
            profile: 'Thông Tin Cá Nhân',
            teaching: 'Giảng Dạy',
            research: 'Nghiên Cứu'
        };
        
        container.innerHTML = `
            <div class="page-header" style="background: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h1 style="color: #667eea; margin-bottom: 10px;">✍️ ${pageNames[page]}</h1>
                <p style="color: #666;">Blog cá nhân và chia sẻ kiến thức</p>
            </div>
            
            <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <p style="color: #666; line-height: 1.8;">
                    Nội dung sẽ được tải từ file <code>data/blog/${page}.json</code>
                </p>
            </div>
        `;
    },
    
    renderSampleData(container, page) {
        this.data = {};
        this.render(container, page);
    }
};

// Export for use in index.html
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { App, Router };
}
