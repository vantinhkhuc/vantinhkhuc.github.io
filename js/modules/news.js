// ============================================
// FILE: js/modules/news.js (Template)
// ============================================

window.newsModule = {
    name: 'news',
    data: null,
    
    async init(params, container) {
        console.log('📰 Loading News Module...', params);
        
        const category = params.category || 'world';
        
        try {
            // Load data
            this.data = await App.loadData(`news/${category}.json`);
            
            // Render
            this.render(container, category);
        } catch (error) {
            // Use sample data if file not found
            console.warn('Using sample data for news');
            this.renderSampleData(container, category);
        }
    },
    
    render(container, category) {
        const categoryNames = {
            world: 'Thế Giới',
            vietnam: 'Việt Nam',
            sports: 'Thể Thao'
        };
        
        const articles = this.data.articles || [];
        
        container.innerHTML = `
            <div class="page-header" style="background: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h1 style="color: #667eea; margin-bottom: 10px;">📰 Tin Tức ${categoryNames[category]}</h1>
                <p style="color: #666;">Cập nhật: ${App.formatDate(this.data.lastUpdate)}</p>
            </div>
            
            <div class="news-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px;">
                ${articles.map(article => `
                    <article class="news-card" style="background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.05); transition: transform 0.3s;">
                        ${article.image ? `<img src="${article.image}" alt="${article.title}" style="width: 100%; height: 200px; object-fit: cover;">` : ''}
                        <div style="padding: 20px;">
                            <h3 style="color: #333; margin-bottom: 10px; font-size: 20px;">${article.title}</h3>
                            <p style="color: #666; margin-bottom: 15px; line-height: 1.6;">${App.truncateText(article.summary, 150)}</p>
                            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; color: #999;">
                                <span>📅 ${article.date}</span>
                                <span>👤 ${article.author}</span>
                            </div>
                            ${article.tags ? `
                                <div style="margin-top: 15px; display: flex; gap: 8px; flex-wrap: wrap;">
                                    ${article.tags.map(tag => `
                                        <span style="background: #f0f0f0; padding: 4px 12px; border-radius: 15px; font-size: 12px;">#${tag}</span>
                                    `).join('')}
                                </div>
                            ` : ''}
                        </div>
                    </article>
                `).join('')}
            </div>
        `;
    },
    
    renderSampleData(container, category) {
        const sampleArticles = [
            {
                title: 'Tiêu đề tin tức mẫu 1',
                summary: 'Đây là nội dung tóm tắt của bài viết. Thông tin chi tiết sẽ được cập nhật sau.',
                author: 'Admin',
                date: '2025-10-05',
                tags: ['kinh-te', 'tai-chinh']
            },
            {
                title: 'Tiêu đề tin tức mẫu 2',
                summary: 'Nội dung mẫu cho bài viết thứ hai. Vui lòng cập nhật file JSON để hiển thị dữ liệu thực.',
                author: 'Admin',
                date: '2025-10-05',
                tags: ['chung-khoan']
            }
        ];
        
        this.data = {
            lastUpdate: new Date().toISOString(),
            articles: sampleArticles
        };
        
        this.render(container, category);
    }
};
