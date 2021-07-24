#! python3

import random

def hangman(word):
#定義
	#初期値
	word_t = word
	echo1 = []
	for c in word:
		echo1.append("_")
	
	word_t = []
	for x in word:
		word_t.append(x)

	#ハングマンの初期値
	hangman = [
	"      o     ",
	"     /|\    ",
	"      |     ",
	"     / \    "]

	#試行回数
	challenge = 1
	
	#失敗階数
	shippai = 0
	
	#あたり文字数
	atari = 0
	
	print("ハングマンゲームへようこそ")
	while shippai < 4:
		print("単語を当ててください。単語のうち1文字を入れてください。([_]の部分を当ててね！")
		print("現在のあたり具合")
		print(echo1)
		a = input()
		n = 0
		for d in word_t:
			n = n+1
			if a == d:
				echo1[n-1] = a
				print("1文字あたり!")
				atari = atari + 1
				word_t[n-1] = "_"
				break
			if n == len(word):
				print("はずれ！")
				shippai = shippai + 1
				e = 0
				while e < shippai:
					print(hangman[e])
					e = e+1
		if atari == len(word):
			print("すべての文字が当たりました。おめでとうございます！")
			print("正解は、「" + word + "」でした")
			print("これで終了です。お疲れさまでした。")
			break
	if shippai == 4:
		print("残念でした。もう一度チャレンジしてくださいね。")

#実行
#単語の選択
words = ["dog","cat","bird","ant"]
kotoba = words[random.randrange(3)]

hangman(kotoba)
