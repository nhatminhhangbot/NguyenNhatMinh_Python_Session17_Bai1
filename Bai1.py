raw_logs = []
processed_logs = []

def clean_raw_logs():
    global raw_logs
    print("\n--- NẠP DỮ LIỆU LOG ---")
    raw_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ").strip()
    if not raw_input:
        print("Dữ liệu nhập vào không được để trống.")
        return
    
    remove_chars = "!@#$"
    trans_table = str.maketrans("", "", remove_chars)
    cleaned_input = raw_input.translate(trans_table)

    raw_logs = [log.strip() for log in cleaned_input.split(";") if log.strip()]
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

def filter_logs():
    global raw_logs, processed_logs
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return
    
    processed_logs = [log for log in raw_logs if "ERROR" in log.upper() or "CRITICAL" in log.upper()]

    print("\n--- LỌC CẢNH BÁO ---")
    if not processed_logs:
        print("Không tìm thấy cảnh báo nguy hiểm nào.")
    else:
        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
        for log in processed_logs:
            print(f"- {log}")

def mask_ip_addresses():
    global processed_logs
    if not processed_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return
    
    masked_list = []
    for log in processed_logs:
        words = log.split()
        new_words = []

        for word in words:
            if "." in word and len(word.split(".")) == 4:
                ip_parts = word.split(".")
                ip_parts[2] = "*"
                ip_parts[3] = "*"
                masked_word = ".".join(ip_parts)
                new_words.append(masked_word)
            else:
                new_words.append(word)

        masked_log = " ".join(new_words)
        masked_list.append(masked_log)

    print("\n--- MÃ HÓA IP ---")
    print("Báo cáo log an toàn:")
    for index, log in enumerate(masked_list, 1):
        print(f"{index}. {log}")

    return masked_list

def main():
    while True:
        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")
        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            clean_raw_logs()
        elif choice == "2":
            filter_logs()
        elif choice == "3":
            mask_ip_addresses()
        elif choice == "4":
            print("Đã đóng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4!")

if __name__ == "__main__":
    main()