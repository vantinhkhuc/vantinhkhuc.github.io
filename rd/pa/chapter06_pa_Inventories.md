# SCRIPT BÀI GIẢNG: KẾ TOÁN HÀNG TỒN KHO
## (INVENTORIES - Chapter 6)

---

## BUỔI 1 (150 phút)

### PHẦN 1: MỞ ĐẦU (15 phút)

#### **Slide 1-2: Giới thiệu**

Chào các em! Hôm nay chúng ta sẽ bắt đầu Chương 6 - một trong những chương quan trọng nhất của môn Nguyên lý Kế toán: **Kế toán Hàng tồn kho**.

Các em có biết không, đối với doanh nghiệp thương mại và sản xuất, hàng tồn kho thường chiếm **30-50%** tổng tài sản. Vì vậy, quản lý tốt hàng tồn kho là yếu tố sống còn quyết định sự thành bại của doanh nghiệp.

Sau 2 buổi học này, các em sẽ hiểu:
- Cách phân loại và xác định hàng tồn kho
- Các phương pháp tính giá khác nhau và khi nào nên dùng
- Ảnh hưởng của sai sót tồn kho
- Cách phân tích hiệu quả quản lý tồn kho

Đặc biệt quan trọng với các em ngành Thương mại điện tử, vì quản lý tồn kho trong TMĐT có nhiều đặc thù riêng!

---

#### **Slide 3: Câu chuyện Komatsu**

Trước khi vào bài, thầy/cô muốn kể cho các em nghe về **Komatsu** - một công ty Nhật Bản sản xuất máy móc xây dựng khổng lồ.

*(Đọc nội dung story)*

Các em thấy không, Komatsu sản xuất những chiếc máy ủi D575 - lớn nhất thế giới. Hãy tưởng tượng nếu họ để 10 chiếc máy ủi như vậy nằm trong kho, giá trị có thể lên đến **hàng chục triệu USD**! 

Chi phí lưu kho khổng lồ, nhưng nếu không có hàng khi khách cần thì cũng mất doanh số. Đó là nghệ thuật cân bằng trong quản lý tồn kho.

Komatsu làm tốt đến mức họ thành lập cả công ty riêng - **Komatsu Logistics** - để giúp các công ty khác quản lý tồn kho. Thật tuyệt phải không?

---

### PHẦN 2: PHÂN LOẠI VÀ XÁC ĐỊNH HÀNG TỒN KHO (40 phút)

#### **Slide 4: Tầm quan trọng**

Tại sao quản lý tốt hàng tồn kho lại quan trọng đến vậy?

**Lợi ích khi quản lý tốt:**
- Luôn có hàng khi khách cần → Không mất doanh số
- Không tồn kho quá nhiều → Tiết kiệm chi phí
- Dòng tiền lưu chuyển tốt → Kinh doanh hiệu quả

**Nhưng nếu quản lý kém:**
- Tồn kho quá cao → Vốn bị ứ đọng, có thể phải vay ngân hàng
- Tồn kho quá thấp → Thiếu hàng, khách chuyển sang đối thủ
- Hàng lỗi thời, hư hỏng → Thua lỗ

Đặc biệt với các em làm TMĐT, khách hàng online rất "nhạy cảm". Họ đặt hàng hôm nay, muốn nhận ngày mai. Nếu bạn báo "hết hàng", họ click sang shop khác chỉ trong **3 giây**!

---

#### **Slide 5-6: Phân loại hàng tồn kho**

Bây giờ chúng ta tìm hiểu cách phân loại hàng tồn kho.

**Đối với Doanh nghiệp Thương mại** (như các em sẽ làm việc sau này):
- Chỉ có **MỘT loại**: Hàng hóa (Merchandise Inventory)
- Ví dụ: Shopee, Lazada, cửa hàng thời trang, siêu thị...

**Đối với Doanh nghiệp Sản xuất** (như Vinamilk, Komatsu):
- **Ba loại:**
  1. **Thành phẩm** (Finished Goods): Đã sản xuất xong, sẵn sàng bán
  2. **Sản phẩm dở dang** (Work in Process): Đang làm dở
  3. **Nguyên vật liệu** (Raw Materials): Chưa đưa vào sản xuất

Các em nhớ hai đặc điểm chung của hàng tồn kho:
1. **Công ty SỞ HỮU**
2. **SẴN SÀNG để bán** trong hoạt động kinh doanh bình thường

---

#### **Slide 7-8: Ví dụ Komatsu & Báo cáo**

Quay lại ví dụ Komatsu. Họ phân loại như thế nào?

*(Giải thích chi tiết ví dụ Gao TVs)*

**Cách tính:**
- So sánh từng mặt hàng: Giá gốc vs NRV
- Chọn giá THẤP HƠN cho mỗi mặt hàng
- Cộng tổng lại

**Kết quả:** 
- TV màn phẳng: Chọn NRV (550 < 600)
- Radio vệ tinh: Chọn Giá gốc (90 < 104)
- Đầu DVD: Chọn NRV (48 < 50)
- Đĩa DVD: Chọn Giá gốc (5 < 6)

**Tổng:** NT$155,800

**Khi nào áp dụng LCNRV?**
- Công nghệ thay đổi (điện thoại, máy tính)
- Thời trang thay đổi (quần áo)
- Hàng hư hỏng, lỗi thời
- Cạnh tranh giá

---

#### **Slide 41-43: Inventory Turnover & Days in Inventory**

Bây giờ chúng ta học cách **phân tích** hàng tồn kho.

**Chỉ số 1: Inventory Turnover (Vòng quay Hàng tồn kho)**

Đo lường: Công ty bán hết và thay thế tồn kho bao nhiêu lần trong năm?

**Công thức:**
```
Inventory Turnover = Giá vốn hàng bán / Tồn kho bình quân
```

*(Tính toán cho Esprit Holdings)*

Kết quả: **3.7 lần/năm**

**Ý nghĩa:** Esprit bán hết và thay thế tồn kho 3.7 lần trong năm.

---

**Chỉ số 2: Days in Inventory (Số ngày tồn kho)**

Đo lường: Trung bình hàng nằm trong kho bao nhiêu ngày?

**Công thức:**
```
Days in Inventory = 365 / Inventory Turnover
```

Esprit: 365 / 3.7 = **99 ngày**

**Ý nghĩa:** Trung bình, hàng tồn kho của Esprit nằm trong kho khoảng 99 ngày từ khi nhập đến khi bán.

---

**Phân tích:**

**Vòng quay CAO / Số ngày THẤP = TỐT:**
- Hàng bán nhanh
- Ít vốn ứ đọng
- Giảm chi phí lưu kho
- Quản lý hiệu quả

**NHƯNG:**
Vòng quay QUÁ CAO cũng nguy hiểm:
- Có thể thiếu hàng (stock-outs)
- Mất khách hàng
- Mất doanh số

→ Phải TÌM ĐIỂM CÂN BẰNG!

---

#### **Slide 43: Case Study Sony**

Bây giờ thầy/cô kể cho các em nghe về Sony.

*(Kể case study chi tiết)*

**Giai đoạn 1:** Sony cắt giảm tồn kho
- Days in inventory: 61 → 38 ngày
- Nhà phân tích: 👍 Tốt!

**Giai đoạn 2:** Sony tăng tồn kho đột ngột
- Muốn bán 25 triệu TV (tăng 60%)
- Days in inventory: 59 ngày
- Nhà phân tích: 😟 Lo ngại!

**Lo ngại gì?**
- Tồn kho quá cao
- Có thể phải giảm giá mạnh
- Lỗ từ giảm giá rất nặng

**Sony nói:** Mức tồn kho hợp lý!

**Các em nghĩ sao?** Ai đúng?

Thực ra, đây là bài toán khó. Phải cân nhắc:
- Dự báo thị trường
- Khả năng sản xuất
- Chiến lược kinh doanh
- Cạnh tranh

---

#### **Slide 47: So sánh ngành**

Một điều quan trọng: **Mỗi ngành có mức tồn kho "chuẩn" khác nhau!**

*(Trình bày bảng so sánh)*

**Siêu thị/Thực phẩm:** 5-15 ngày
- Tại sao? Hàng tươi sống, dễ hỏng
- Ví dụ: Vinmart phải bán nhanh

**Thời trang nhanh:** 30-60 ngày
- Tại sao? Xu hướng thay đổi nhanh
- Ví dụ: Zara, H&M

**Điện tử:** 40-90 ngày
- Tại sao? Công nghệ lỗi thời nhanh
- Ví dụ: Thế Giới Di Động

**Ô tô:** 60-90 ngày
- Tại sao? Giá trị cao, ít lỗi thời
- Ví dụ: Toyota, Honda

**Trang sức:** 100-200 ngày
- Tại sao? Giá trị cao, không lỗi thời
- Ví dụ: PNJ

**Máy móc công nghiệp:** 120-300 ngày
- Tại sao? Đặc thù, sản xuất theo đơn
- Ví dụ: Komatsu

**Bài học:** KHÔNG nên so sánh trực tiếp giữa các ngành khác nhau!

---

#### **Slide 48-49: Ứng dụng trong TMĐT & Công nghệ**

Các em học TMĐT, vậy đặc thù quản lý tồn kho trong TMĐT là gì?

**Đặc thù:**
1. **Đa kênh:** Website + App + Marketplace + Cửa hàng
2. **Giao hàng nhanh:** 1-3 ngày, có khi trong ngày!
3. **Kỳ vọng cao:** Luôn có hàng, không chấp nhận "hết hàng"
4. **Dễ so sánh:** Click sang đối thủ chỉ 3 giây!

**Thách thức:**

**1. Đồng bộ tồn kho đa kênh:**
- Cập nhật real-time
- Tránh overselling (bán quá số lượng có)
- Ví dụ: Bán trên Shopee, Lazada, website cùng lúc

**2. Dự báo nhu cầu:**
- Phân tích big data
- Xu hướng mùa vụ (Tết, Black Friday, 11/11...)
- Flash sale, khuyến mãi đột xuất

**3. Quản lý kho phân tán:**
- Nhiều kho vùng miền (Hà Nội, TP.HCM, Đà Nẵng...)
- Tối ưu chi phí vận chuyển
- Ship from store (giao từ cửa hàng gần nhất)

**4. Xử lý hàng trả lại:**
- Tỷ lệ trả hàng cao hơn offline (10-30%)
- Kiểm tra chất lượng
- Tái nhập kho hoặc thanh lý

---

**Công nghệ hỗ trợ:**

**Truyền thống:**
- Mã vạch (Barcode): Phổ biến nhất, chi phí thấp
- ERP Systems: SAP, Oracle...

**Hiện đại:**
- **RFID:** Không cần quét, quét hàng loạt
- **IoT & AI:** Theo dõi real-time, dự báo thông minh
- **Blockchain:** Truy xuất nguồn gốc
- **Machine Learning:** Dự báo nhu cầu chính xác
- **Drone & Robot:** Kiểm kê tự động

---

**⏰ NGHỈ GIẢI LAO 10 PHÚT**

---

### PHẦN 7: BÀI TẬP TỔNG HỢP (40 phút)

#### **Slide 52-54: Bài tập 1**

Bây giờ chúng ta làm bài tập tổng hợp để củng cố kiến thức!

*(Đọc đề bài tập 1 - Công ty ABC)*

**Phân tích:**
- Tổng hàng: 450 đơn vị
- Đã bán: 300 đơn vị
- Còn lại: 150 đơn vị

**Yêu cầu 1: FIFO**

Các em nhớ không? FIFO là "First-In, First-Out" - Nhập trước, xuất trước.

Vậy tồn kho 150 đơn vị sẽ là những đơn vị mua **GẦN ĐÂY NHẤT**.

*(Hướng dẫn tính toán từng bước)*

Lấy từ lô mua cuối:
- 25/3: 150 đơn vị @ €60 = €9,000 ✓

Giá vốn = €25,000 - €9,000 = **€16,000**

---

**Yêu cầu 2: Average-Cost**

Công thức: Tổng giá trị / Tổng số lượng

€25,000 / 450 = **€55.56**

- Tồn kho: 150 × €55.56 = **€8,334**
- Giá vốn: €25,000 - €8,334 = **€16,666**

---

**Yêu cầu 3: Lập Income Statement**

*(Trình bày và so sánh hai phương pháp)*

**Phân tích:**
- FIFO: LN cao hơn €666
- Tại sao? Vì giá đang TĂNG, FIFO dùng giá CŨ cho giá vốn
- Average: Giá vốn cao hơn → LN thấp hơn → Thuế thấp hơn

**Yêu cầu 4: Inventory Turnover**

FIFO: 16,000 / [(5,000 + 9,000)/2] = **2.29 lần**
Average: 16,666 / [(5,000 + 8,334)/2] = **2.50 lần**

Các em để ý: Average có vòng quay cao hơn một chút!

---

#### **Slide 55-57: Bài tập 2**

Tiếp theo, chúng ta làm bài tập về **SAI SÓT**.

*(Đọc đề bài tập 2 - Công ty XYZ)*

Đây là bài tập phức tạp hơn vì có **HAI SAI SÓT**:
1. Tồn cuối 2023 THỪA ¥30,000
2. Tồn cuối 2024 THIẾU ¥20,000

**Phân tích từng sai sót:**

**Sai sót 1:**
- 2023: Tồn cuối THỪA → Giá vốn THIẾU → LN THỪA ¥30k
- 2024: Tồn đầu THỪA → Giá vốn THỪA → LN THIẾU ¥30k

**Sai sót 2:**
- 2024: Tồn cuối THIẾU → Giá vốn THỪA → LN THIẾU ¥20k
- 2025: Tồn đầu THIẾU → Giá vốn THIẾU → LN THỪA ¥20k

*(Tính toán chi tiết)*

**Lợi nhuận đúng:**
- 2023: ¥500,000 - ¥30,000 = **¥470,000**
- 2024: ¥600,000 + ¥30,000 - ¥20,000 = **¥610,000**

**Ảnh hưởng đến Vốn CSH:**
- 31/12/2023: THỪA ¥30,000
- 31/12/2024: THIẾU ¥20,000
- 31/12/2025: ĐÚNG (tự sửa)

---

### PHẦN 8: THẢO LUẬN & CASE STUDY (25 phút)

#### **Slide 58: Câu hỏi thảo luận**

Bây giờ chúng ta thảo luận một số tình huống thực tế!

**Câu hỏi 1: Lựa chọn phương pháp**

Giả sử các em là CFO của một startup TMĐT bán thời trang. Lạm phát 10-15%/năm. Chọn FIFO hay Average-Cost?

*(Chia nhóm thảo luận 5 phút)*

Các nhóm trình bày!

**Phân tích:**

**Chọn FIFO nếu:**
- Cần thu hút nhà đầu tư (lợi nhuận cao)
- Chuẩn bị IPO
- Muốn vay ngân hàng (tài sản cao)

**Chọn Average-Cost nếu:**
- Cần tiết kiệm thuế (nhiều tiền mặt)
- Ổn định lợi nhuận qua các năm
- Giá biến động mạnh

---

**Câu hỏi 2: JIT có phù hợp?**

*(Chia nhóm phân tích từng trường hợp)*

**a) Shopee, Lazada (Marketplace):**
- PHÙ HỢP một phần
- Không giữ hàng, kết nối người bán - người mua
- Nhưng phải có kho fulfillment cho seller

**b) Thế Giới Di Động:**
- KHÓ áp dụng hoàn toàn
- Khách muốn xem hàng, thử ngay
- Cần tồn kho trưng bày
- Nhưng có thể giảm tồn kho kho hàng

**c) Vinamilk:**
- KHÔNG phù hợp
- Sữa có thời gian sản xuất
- Cần tồn kho an toàn
- Nhưng vẫn cần tối ưu

---

**Câu hỏi 3: Đạo đức nghề nghiệp**

Đây là câu hỏi KHÔNG CÓ đáp án dễ dàng!

**Tình huống:** Sếp yêu cầu "điều chỉnh" tồn kho để đạt chỉ tiêu.

**Các lựa chọn:**

**Làm theo sếp:**
- ❌ Vi phạm đạo đức nghề nghiệp
- ❌ Gian lận báo cáo tài chính
- ❌ Có thể bị truy cứu trách nhiệm pháp lý
- ❌ Mất uy tín, sự nghiệp

**Từ chối:**
- ✅ Giữ vững đạo đức
- ⚠️ Có thể bị sa thải
- ⚠️ Khó khăn tài chính ngắn hạn

**Giải pháp khác:**
- Báo cáo lên cấp trên của sếp
- Tham vấn bộ phận pháp lý
- Tham vấn ban kiểm soát
- Tìm việc mới trước khi từ chối

**Quan điểm của thầy/cô:**
KHÔNG BAO GIỜ thỏa hiệp với đạo đức nghề nghiệp! Uy tín mất đi không thể lấy lại.

---

#### **Slide 59: Case Study Việt Nam**

Bây giờ chúng ta xem các công ty Việt Nam làm thế nào!

**1. Thế Giới Di Động:**
- Vòng quay cao: 40-50 ngày
- Chiến lược:
  - Đàm phán chính sách đổi trả với nhà cung cấp
  - Giảm giá nhanh cho hàng cũ
  - Dự báo dựa trên big data
  - Mở rộng liên tục → Luôn cần hàng

**2. Vinamilk:**
- Vòng quay: 30-40 ngày
- Chiến lược:
  - FIFO nghiêm ngặt (hàng có hạn SD)
  - Hệ thống kho lạnh hiện đại
  - Mạng lưới phân phối rộng
  - Giao hàng nhanh

**3. CANIFA:**
- Thời trang theo mùa
- Chiến lược:
  - Flash sale cuối mùa
  - Sản xuất theo đơn hàng (một phần)
  - Outlet cho hàng tồn cũ
  - Phân tích xu hướng để dự báo

Các em thấy không, mỗi công ty có chiến lược riêng phù hợp với ngành của mình!

---

### PHẦN 9: XU HƯỚNG TƯƠNG LAI & KẾT THÚC (15 phút)

#### **Slide 60: Xu hướng tương lai**

**1. Omnichannel Inventory:**
- Thống nhất tồn kho tất cả kênh
- Mua online, nhận tại cửa hàng (BOPIS)
- Trả hàng mua online tại offline
- Ship from store

Ví dụ: Các em mua hàng trên app Vinmart, nhận tại siêu thị gần nhất trong 2 giờ!

**2. AI và Machine Learning:**
- Dự báo nhu cầu thông minh
- Định giá động theo cung cầu
- Phát hiện gian lận
- Tối ưu hóa tồn kho

**3. Blockchain:**
- Minh bạch chuỗi cung ứng
- Chống hàng giả
- Truy xuất nguồn gốc
- Quan trọng: Thực phẩm, dược phẩm

**4. Sustainable Inventory:**
- Giảm lãng phí
- Tái chế, tái sử dụng
- Kinh tế tuần hoàn
- ESG reporting

---

#### **Slide 61: Kỹ năng cần có**

Để thành công trong lĩnh vực này, các em cần:

**Kiến thức chuyên môn:**
- Nguyên lý kế toán ✓ (đang học)
- Kế toán quản trị
- Phân tích tài chính
- Quản lý chuỗi cung ứng
- Marketing & Bán hàng

**Kỹ năng công nghệ:**
- Excel nâng cao (pivot table, VLOOKUP...)
- Power BI / Tableau (trực quan hóa dữ liệu)
- ERP Systems (SAP, Oracle...)
- SQL cơ bản (truy vấn dữ liệu)
- Hiểu về AI/ML

**Kỹ năng mềm:**
- Tư duy phân tích
- Giải quyết vấn đề
- Ra quyết định dựa trên dữ liệu
- Giao tiếp hiệu quả
- Làm việc nhóm
- **ĐẠO ĐỨC NGHỀ NGHIỆP** (quan trọng nhất!)

**Định hướng nghề nghiệp:**
- Kế toán viên
- Kiểm toán viên
- Phân tích tài chính
- Quản lý tồn kho / Supply Chain Manager
- E-commerce Manager
- Data Analyst

---

#### **Slide 62: Kết thúc**

Vậy là chúng ta đã kết thúc Chương 6!

**TÓM TẮT LẠI:**

**1. Phân loại & Xác định:**
- DN Thương mại: Hàng hóa
- DN Sản xuất: 3 loại
- FOB và Hàng gửi bán

**2. Phương pháp tính giá:**
- FIFO: Giá mới cho tồn kho
- Average-Cost: Ổn định hơn
- Chọn dựa trên: Income, Balance Sheet, Tax

**3. Sai sót:**
- Ảnh hưởng 2 kỳ
- Tự triệt tiêu sau 2 năm
- Nhưng phải sửa ngay!

**4. Phân tích:**
- Inventory Turnover
- Days in Inventory
- So sánh trong cùng ngành

**5. Đạo đức:**
- KHÔNG BAO GIỜ thỏa hiệp!

---

**Câu nói để nhớ:**

> "Khi bạn sản xuất thiết bị để di chuyển núi,
> mọi thứ khác trở nên dễ dàng."
> - Komatsu

**Ý nghĩa:** Nếu bạn làm tốt những việc khó (quản lý tồn kho khổng lồ), những việc khác sẽ dễ dàng hơn!

---

**BÀI TẬP VỀ NHÀ:**

1. Làm tất cả bài tập cuối chương (E6.3 - E6.13)
2. Đọc trước Chương 7
3. Chuẩn bị cho bài kiểm tra giữa kỳ
4. Tìm hiểu thêm về một công ty TMĐT và phân tích chiến lược quản lý tồn kho của họ

---

**CÂU HỎI?**

Các em có câu hỏi gì không?

*(Trả lời câu hỏi của sinh viên)*

---

**THÔNG BÁO:**

- Tuần sau: Chương 7 - Internal Control & Cash
- Bài kiểm tra giữa kỳ: 2 tuần nữa (Chương 1-7)
- Office hours: Thứ 3 & Thứ 5, 14h-16h
- Email: [email giảng viên]

---

**KẾT THÚC**

Cảm ơn các em đã tham gia nhiệt tình!

Chúc các em học tốt và thành công!

Hẹn gặp lại tuần sau! 👋

---

## PHỤ LỤC: MỘT SỐ GỢI Ý GIẢNG DẠY

### Mẹo giảng dạy hiệu quả:

**1. Tương tác:**
- Đặt câu hỏi thường xuyên
- Gọi tên sinh viên
- Sử dụng Mentimeter hoặc Kahoot cho quiz
- Khuyến khích thảo luận nhóm

**2. Ví dụ thực tế:**
- Dùng ví dụ công ty Việt Nam (Thế Giới Di Động, Vinamilk...)
- Kết nối với kinh nghiệm mua sắm của sinh viên
- Case study từ báo chí

**3. Công nghệ:**
- Demo một phần mềm quản lý tồn kho đơn giản
- Cho xem video ngắn về kho hàng tự động của Amazon
- Sử dụng Google Sheets để tính toán real-time

**4. Đánh giá:**
- Quiz ngắn đầu/cuối buổi (5 phút)
- Bài tập nhóm trong lớp
- Thảo luận case study
- Phát biểu ý kiến

**5. Điều chỉnh tốc độ:**
- Quan sát phản ứng của sinh viên
- Nếu khó: Giải thích lại bằng ví dụ khác
- Nếu dễ: Thêm bài tập nâng cao
- Dành thời gian cho câu hỏi

### Các điểm cần nhấn mạnh:

**⚠️ Dễ nhầm lẫn:**
- FOB Shipping Point vs Destination
- FIFO trong định kỳ vs thường xuyên (kết quả giống nhau)
- Average trong định kỳ vs thường xuyên (kết quả khác nhau)
- Ảnh hưởng của sai sót qua 2 năm

**💡 Quan trọng nhất:**
- Đạo đức nghề nghiệp
- Ảnh hưởng của phương pháp tính giá đến thuế và lợi nhuận
- Sai sót tồn kho ảnh hưởng đến 2 kỳ

**🎯 Kỹ năng thực hành:**
- Tính toán FIFO và Average-Cost
- Phân tích Inventory Turnover
- Xác định quyền sở hữu hàng hóa
- Áp dụng LCNRV

### Câu hỏi dự kiến từ sinh viên:

**Q: Tại sao IFRS cấm LIFO?**
A: Vì LIFO làm tồn kho trên BCDKT không phản ánh giá trị gần đây, có thể sai lệch lớn trong thời kỳ lạm phát cao.

**Q: Công ty có thể đổi phương pháp tính giá không?**
A: Có, nhưng phải công bố rõ ràng, giải thích lý do và ảnh hưởng. Không nên đổi thường xuyên.

**Q: Phương pháp nào tốt nhất?**
A: KHÔNG có phương pháp "tốt nhất". Tùy thuộc vào ngành, chiến lược, và mục tiêu của công ty.

**Q: Trong TMĐT, nên dùng FIFO hay Average?**
A: Thường dùng FIFO vì dễ theo dõi và phù hợp với luồng hàng thực tế. Nhưng nếu hàng đồng nhất (như điện thoại cùng model), Average cũng được.

**Q: JIT có phù hợp với startup TMĐT không?**
A: Phụ thuộc vào loại hàng. Nếu dropshipping thì tương tự JIT. Nếu tự giữ kho, cần cân bằng giữa chi phí và khả năng giao hàng nhanh.

---

## CHECKLIST CHUẨN BỊ BUỔI HỌC:

### Trước buổi học:
- [ ] In handout cho sinh viên
- [ ] Chuẩn bị bài tập trên bảng
- [ ] Test slideshow
- [ ] Chuẩn bị câu hỏi quiz
- [ ] Kiểm tra projector/màn hình

### Trong buổi học:
- [ ] Điểm danh
- [ ] Review buổi trước (5 phút)
- [ ] Đặt câu hỏi thường xuyên
- [ ] Gọi tên sinh viên
- [ ] Nghỉ giải lao đúng giờ
- [ ] Tóm tắt cuối buổi

### Sau buổi học:
- [ ] Trả lời email sinh viên
- [ ] Đăng tài liệu lên hệ thống
- [ ] Chuẩn bị bài tập về nhà
- [ ] Note lại phần nào cần cải thiện
- [ ] Chuẩn bị cho buổi sau

---

**CHÚC GIẢNG VIÊN GIẢNG DẠY THÀNH CÔNG! 
