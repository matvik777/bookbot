def main():
    path_to_file = "books/frankenstein.txt"
    
    # Открытие файла и перевод текста в нижний регистр
    with open(path_to_file, "r", encoding="utf-8") as f:
        file_contents = f.read().lower()
    
    # Подсчёт символов
    count_s = {}
    for char in file_contents:
        if char.isalpha():  # Проверяем, что символ является буквой
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
    
    # Сортировка символов по частоте
    sorted_count_s = sorted(count_s.items(), key=lambda item: item[1], reverse=True)
    
    # Подсчёт слов
    count_w = len(file_contents.split())
    
    # Вывод отчёта
    print(f"--- Begin report of {path_to_file} ---")
    print(f" {count_w} words found in the document\n")
    
    for char, count in sorted_count_s:
        print(f"The '{char}'  character was found {count} times")
    
    print("--- End report ---")
    

if __name__ == "__main__":
    main()
