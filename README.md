
Đăng nhập Git bằng mail FPT để trở thành collaborator của project. (1) Set-up

Tại git bash, cd 1 thư mục trống
Chạy lệnh git clone https://github.com/hunglthe150135/hello-world.git

Mở project tại IDE (PyCharm, Visual Studio Code), chạy 3 lệnh sau trên Terminal: git branch ngohieu (đặt theo tên của mọi người) git checkout ngohieu git push --set-upstream origin ngohieu Lưu ý: Tuyệt đối không code trên branch khác. Luôn kiểm tra xem mình đang ở branch nào trước khi code bằng cách chạy lệnh git branch xem mình đang ở branch nào.
(2) Kéo code về Trong quá trình code có khả năng sẽ có thay đổi code trên branch chính từ việc mình sửa khung, hoặc mình merge code từ branch khác về branch chính. Muốn kéo code, chạy bộ lệnh sau trên Terminal git stash git pull origin hunglt (tên branch chính) git stash apply Kiểm tra Terminal có conflict code hay không. Conflict code đến từ việc trên cùng 1 file có hơn 1 người cùng sửa, vậy nên khi kéo code về phải resolve conflict để tránh mất code của bản thân và của người khác. Resolve conflict hoàn toàn thực hiện bằng tay (manually) nên mọi người chủ động liên hệ nhau để xem phần nào giữ lại, phần nào bỏ đi.


(3) Đẩy code Trước khi đẩy code bắt buộc phải kéo code về. Sau khi kéo code về và resolve conflict nếu có, chạy 03 lệnh sau trên Terminal git add . git commit -m "lời nhắn bất kỳ nào đó để nhận biết" git push Sau đó qua repo trên github.com (https://github.com/hunglthe150135/hello-world.git), vào branch của mình, ấn Create pull request và thông báo với mình là đã đẩy code trên Messenger. Sau khi mình kiểm tra code thấy code được và không có conflict thì mình sẽ merge code lên branch chính, còn nếu không thì mình sẽ reject và mọi người tiếp tục sửa code cho lần đẩy code sau.
