# Bé Vui Học — bản dựng lại (clone tham khảo)

Bản dựng lại giao diện và trải nghiệm của **vuihochocvui.com** (ứng dụng học miễn phí
cho bé 3–6 tuổi), kèm 14 hoạt động học & chơi chạy được thật trên trình duyệt.

## Chạy thử

Cách 1 — nhấp đôi `run.bat` (cần Python), rồi mở http://127.0.0.1:8123

Cách 2 — `python serve.py 8123` nếu muốn tự chọn cổng.

Cách 3 — mở thẳng `index.html` bằng Chrome/Edge (một số trình duyệt chặn
`localStorage` với `file://`, khi đó số sao sẽ không được lưu).

### Dùng trên điện thoại (cùng Wi-Fi)

1. Chạy `run.bat` (hoặc `python serve.py 8123`) trên máy tính.
2. Máy in ra địa chỉ dạng `http://192.168.x.x:8123` — mở địa chỉ đó trên
   điện thoại (cùng mạng Wi-Fi).
3. Trên iPhone/Android: menu trình duyệt → "Thêm vào màn hình chính" để cài
   như ứng dụng (PWA, có offline sau lần mở đầu).

> Lưu ý: điện thoại và máy tính phải cùng mạng Wi-Fi. Nếu không thấy, kiểm tra
> tường lửa Windows cho phép Python trên mạng riêng (Private network).

## Có gì trong này

| Đường dẫn | Nội dung |
| --- | --- |
| `index.html` | Màn hình chào: poster 941×1672, mặt trời, 4 bạn nhân vật, logo, khẩu hiệu, 3 chủ đề, nút Bắt đầu, khu học & chơi |
| `bai-hoc-cho-be.html` | Danh sách 9 hoạt động học, lọc theo môn (Tiếng Việt / Toán / Tiếng Anh / Trò chơi) |
| `tieng-viet.html` | Giới thiệu học Tiếng Việt + mẹo học cùng con |
| `toan.html` | Giới thiệu Toán, tư duy và 4 hoạt động toán |
| `tieng-anh.html` | Từ vựng tiếng Anh theo chủ đề, có bảng tra từ |
| `tro-choi-cho-be.html` | Giới thiệu khu trò chơi |
| `goc-bo-me.html` | Góc bố mẹ: sao, số câu, tỉ lệ đúng, lượt chơi và những chữ bé đã luyện |
| `about.html` | Giới thiệu, quyền riêng tư, khu vực chia sẻ |
| `assets/css` | `base.css` (dùng chung), `home.css` (poster), `games.css` (khu học & chơi) |
| `assets/js` | `brand.js` (3 bộ thương hiệu), `lang.js` (5 ngôn ngữ), `progress.js` (tiến trình), `games.js` (14 hoạt động), `site.js` (nút, hộp thoại, chia sẻ, offline) |
| `assets/img` | Hình ảnh, biểu trưng SVG và ảnh đại diện `avatar.jpg` |

## Mười bốn hoạt động đã chạy được

**Học**

1. **Học chữ** — nhận biết chữ cái, có nút nghe (Web Speech API) đọc chữ và từ.
2. **Ghép vần** — ghép phụ âm với nguyên âm thành tiếng (b + a = ba).
3. **Tập viết** — đồ theo nét mờ 29 chữ cái viết hoa trên bảng vẽ (canvas).
4. **Học số** — đếm hình rồi chọn số đúng (1–10).
5. **Đếm đến 20** — đếm nhiều đồ vật hơn, luyện số đến 20.
6. **Hình dạng** — nhận biết hình tròn, vuông, tam giác, ngôi sao…

**Chơi**

6. **Cộng trừ** — cộng/trừ trong phạm vi 10, có nhóm hình để bé đếm.
7. **So sánh** — chọn dấu `>`, `<` hay `=` cho hai nhóm hình.
8. **Dãy số** — tìm số còn thiếu trong dãy đếm cách 1 hoặc cách 2.
9. **Tiếng Anh** — 4 chủ đề (động vật, trái cây, màu sắc, số đếm), nghe phát âm mẫu.
10. **Trò chơi trí nhớ** — lật 12 thẻ, tìm 6 cặp hình.
11. **Tìm khác biệt** — quan sát 4 hình và chỉ ra hình khác với các hình còn lại.
12. **Vẽ tự do** — bảng vẽ tự do, 8 màu và 3 cỡ bút, bé vẽ theo ý thích.
13. **Đồng hồ** — xem kim giờ và kim phút, chọn giờ đúng.

Mỗi câu đúng nhận 1 sao, hoàn thành lượt chơi nhận thêm 2 sao. Số sao lưu trong
`localStorage` của thiết bị. Âm thanh dùng Web Audio API nên không cần tệp âm thanh.

## Điều hướng nhanh (liên kết sâu)

- `index.html#bat-dau` — mở khu học & chơi
- `index.html#hoc-chu` — vào thẳng trò Học chữ
- `index.html#ghep-van` — vào thẳng trò Ghép vần
- `index.html#tap-viet` — vào thẳng trò Tập viết
- `index.html#hoc-so` — vào thẳng trò Học số
- `index.html#cong-tru` — vào thẳng trò Cộng trừ
- `index.html#so-sanh` — vào thẳng trò So sánh
- `index.html#day-so` — vào thẳng trò Dãy số
- `index.html#hinh-dang` — vào thẳng trò Hình dạng
- `index.html#tieng-anh` — vào thẳng trò Tiếng anh
- `index.html#tri-nho` — vào thẳng trò trí nhớ
- `index.html#tim-khac-biet` — vào thẳng trò Tìm khác biệt
- `index.html#ve-tu-do` — vào thẳng trò Vẽ tự do

## Thương hiệu, ngôn ngữ và offline

- **3 bộ thương hiệu** (`assets/js/brand.js`): Bé Thông Minh, Mầm Xanh (mặc định,
  đúng bảng màu gốc), Tí Hon. Đổi thương hiệu sẽ đổi màu, tên và logo nội tuyến,
  nhưng **không ghi đè tiêu đề SEO** của từng trang.
- **5 ngôn ngữ** cho màn hình chào (`assets/js/lang.js`): Tiếng Việt, English,
  日本語, 한국어, 简体中文.
- **Học offline**: `sw.js` lưu sẵn các tệp cốt lõi sau lần mở đầu tiên. Nhớ tăng
  `CACHE` trong `sw.js` mỗi khi sửa CSS/JS để tránh bản cũ.
- **Cài như ứng dụng**: `manifest.json` có `shortcuts` cho Học chữ, Học số,
  Cộng trừ và Trí nhớ.

## Tính năng mới (vòng này)

- **Chế độ tối**: nút 🌙/☀️ trên màn hình chào và thanh công cụ trong khu học & chơi; lưu lựa chọn trong `localStorage`.
- **Bật/tắt âm thanh**: nút 🔊/🔇 tắt Web Audio + giọng đọc; lưu lựa chọn.
- **Huy hiệu**: `goc-bo-me.html` có "Bộ sưu tập huy hiệu" (6 huy hiệu theo sao và tiến trình).
- **2 trò chơi mới**: Đếm đến 20, Đồng hồ (xem kim và chọn giờ).

## Ghi chú

- Đây là bản dựng phục vụ học tập/trình diễn, không phải bản chính thức của
  vuihochocvui.com và không liên kết với chủ sở hữu trang gốc.
- Ảnh OG `assets/img/share-be-vui-hoc.png` là ảnh thương hiệu mới, dựng bằng `_share.html` (đã xoá sau khi xuất ảnh).
- `_icon.html` (dựng biểu trưng) đã xoá sau khi xuất `icon-*.png`.
- `_test.html` và `_mobile.html` là trang dựng thử, đã xoá.
- Font Baloo 2 (SIL Open Font License) lưu cục bộ trong ssets/fonts.
