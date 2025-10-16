// ============================================
// FILE: js/modules/finance.js (Template)
// ============================================

window.financeModule = {
    name: 'finance',
    data: null,
    
    async init(params, container) {
        console.log('💰 Loading Finance Module...', params);
        
        const view = params.view || 'dashboard';
        
        try {
            // Load data
            this.data = await App.loadData(`finance/${view}.json`);
            
            // Render based on view
            this.render(container, view);
        } catch (error) {
            console.warn('Using sample data for finance');
            this.renderSampleData(container, view);
        }
    },
    
    render(container, view) {
        const views = {
            dashboard: this.renderDashboard.bind(this),
            technical: this.renderTechnical.bind(this),
            fundamental: this.renderFundamental.bind(this),
            macro: this.renderMacro.bind(this)
        };
        
        if (views[view]) {
            views[view](container);
        }
    },
    
    renderDashboard(container) {
        container.innerHTML = `
            <div class="page-header" style="background: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h1 style="color: #667eea; margin-bottom: 10px;">📊 Dashboard Thị Trường</h1>
                <p style="color: #666;">Cập nhật: ${App.formatDate(this.data.lastUpdate)}</p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px;">
                ${this.data.markets.map(market => `
                    <div style="background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                        <h3 style="font-size: 14px; color: #666; margin-bottom: 10px;">${market.name}</h3>
                        <div style="font-size: 32px; font-weight: bold; color: #333; margin-bottom: 5px;">${App.formatNumber(market.value)}</div>
                        <div style="font-size: 18px; font-weight: 600; color: ${market.change > 0 ? '#26a69a' : '#ef5350'};">
                            ${market.change > 0 ? '▲' : '▼'} ${Math.abs(market.change).toFixed(2)} (${Math.abs(market.changePercent).toFixed(2)}%)
                        </div>
                    </div>
                `).join('')}
            </div>
            
            <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h2 style="color: #667eea; margin-bottom: 20px;">🚀 Top Cổ Phiếu Tăng</h2>
                <p style="color: #666; font-style: italic;">Dữ liệu sẽ được cập nhật tự động từ file JSON...</p>
            </div>
        `;
    },
    
    renderTechnical(container) {
        container.innerHTML = `
            <div class="page-header" style="background: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h1 style="color: #667eea; margin-bottom: 10px;">📈 Phân Tích Kỹ Thuật</h1>
                <p style="color: #666;">Module đang được phát triển...</p>
            </div>
            
            <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <p style="color: #666; line-height: 1.8;">
                    Tính năng biểu đồ nến, chỉ báo kỹ thuật sẽ được tích hợp từ module đã tạo trước đó.
                    Vui lòng thêm file <code>js/modules/finance.js</code> với code đầy đủ.
                </p>
            </div>
        `;
    },
    
    renderFundamental(container) {
        container.innerHTML = `
            <div class="page-header" style="background: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h1 style="color: #667eea; margin-bottom: 10px;">💼 Phân Tích Cơ Bản</h1>
                <p style="color: #666;">Báo cáo tài chính và chỉ số tài chính</p>
            </div>
        `;
    },
    
    renderMacro(container) {
        container.innerHTML = `
            <div class="page-header" style="background: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                <h1 style="color: #667eea; margin-bottom: 10px;">🌐 Phân Tích Vĩ Mô</h1>
                <p style="color: #666;">Tổng quan kinh tế Việt Nam và Thế giới</p>
            </div>
        `;
    },
    
    renderSampleData(container, view) {
        this.data = {
            lastUpdate: new Date().toISOString(),
            markets: [
                { name: 'VN-Index', value: 1250.5, change: 15.3, changePercent: 1.24 },
                { name: 'HNX-Index', value: 235.8, change: -2.1, changePercent: -0.88 }
            ]
        };
        
        this.render(container, view);
    }
};
