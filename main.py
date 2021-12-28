# import random
#
# # Нові слова з отриманого слова
# if __name__ == '__main__':
#     user_string = input("Enter the word: ")
#     length_word = len(user_string)
#     count_word = 5
#     while count_word > 0:
#         count_word -= 1
#         user_string_copy = user_string
#         word = ""
#         while len(word) < length_word:
#             index = random.randint(0, len(user_string_copy) - 1)
#             word += user_string_copy[index]
#             user_string_copy = user_string_copy[0:index] + user_string_copy[index + 1:]
#         print(word)
#
# if __name__ == '__main__':
#     rouns = 0
#     pc_wins = 0
#     user_wins = 0
#     print("Rock-[1],scizors[2],paper[3]")
#     while rouns < 3:
#         rouns += 1
#         pc_choice = random.randint(1, 3)
#         ans = ""
#         while ans == "1" and ans == "2" and ans == "3":
#
#             ans = input()
#         ans = int(ans)
a = [int(k) for k in input().split()]
counter = 0

for i in a[1:-1]:
    if a.index(a.index(i)-1) < i > a.index(a.index(i)+1):
        counter += 1

print(counter)