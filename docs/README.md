# DT036 Phân tích số nguyên thành tổng không tăng

Mai Đăng Khoa — N24DCDT040 — D24CQDT01-N — INT13185 nhóm 03.
Giảng viên: Hồ Nhựt Minh.

## Yêu cầu và cách chạy trên Windows
Môi trường thực chạy trong Terminal: Python 3.11.15, theo ảnh và log máy cá nhân. Chỉ dùng thư viện chuẩn. Không cần pip install.
Mở VS Code tại thư mục chứa demo.py, mở Terminal PowerShell.
```powershell
python --version
python demo.py --n 4
python demo.py --n 1
python demo.py
python test/run_tests.py --out docs/ket_qua_kiem_tra/kiem_thu_may_ca_nhan.json
python survey.py
```
Nếu máy không có lệnh py nhưng có Python 3, thay `python` bằng `python`.
Linux/macOS dùng `python3`. Nhập mới bằng bàn phím với `demo.py` không đối số.
Ví dụ 1 có thể thêm `--trace` để in vào/ra và quay lui.

## Tổ chức
- src/phan_tich.py: thuật toán chính, kiểm tra đầu vào và bộ đếm.
- demo.py: ví dụ, nhập bàn phím, chạy ca chọn bằng --case.
- test/cases.json: 22 ca, input, expected và mục tiêu đặt trước khi chạy.
- test/run_tests.py: kiểm thử bằng kỳ vọng trực tiếp, bất biến và đối chứng độc lập.
- survey.py: khảo sát ba quy mô hợp lệ.
- docs/ket_qua_kiem_tra/: kết quả kiểm thử, lần vết và khảo sát.
- docs/anh_ket_qua/: nơi đặt A01.png đến A11.png sau khi chụp.

## Hợp đồng và phần tự cài
Input n là số nguyên 1..20; bool, số thực và giá trị ngoài miền bị từ chối. Output gồm nghiệm không tăng theo thứ tự từ điển giảm, số cách, bộ đếm, lần vết tùy chọn. Mở rộng k thuộc 1..n, chỉ lấy nghiệm có k số hạng.
Tự cài bước append → đệ quy với (con−v,v) → pop; không dùng thư viện liệt kê phân hoạch. DP trong test chỉ là đối chứng số nghiệm, không thay thuật toán chính. Bản này giữ toàn bộ nghiệm nên bộ nhớ gồm O(n) làm việc và O(nP(n)) chặn trên cho kết quả. Lần vết tùy chọn có thêm chi phí, nên tắt khi khảo sát.


## Tài liệu tham khảo
Phiếu giao đề tài cá nhân, giáo trình INT1306 và hướng dẫn học phần INT13185 nhóm 03 do giảng viên cung cấp ngày 17/10/2026.

## Đối chiếu phiên bản và minh chứng
Các kết quả trong docs/ket_qua_kiem_tra là kết quả kiểm tra khi chuẩn bị mã, không thay thế ảnh chạy cá nhân A01–A11. Chạy lại trên máy cá nhân để xác nhận phiên bản Python, lưu log và chụp ảnh. Điền SHA C/S, permalink và kết quả thực tế vào ThongTinNop.txt sau khi chốt phiên bản.

## Kết quả máy cá nhân đã lưu
Log kiem_thu_may_ca_nhan.json: 22/22 PASS, 82 phép kiểm, Python 3.11.15. Ảnh A09 gồm A09a.png và A09b.png; A10.png là ảnh clone C chạy VD01. Còn thiếu A11 và kết quả clone S.
