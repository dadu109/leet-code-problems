const input = ["a", "banana", "app", "appl", "ap", "apply", "apple"];

const longestWord = (words) => {
    let longest = ""
    let tmp = ""
    for (let i = 0; i < words.length; i++) {
        tmp = words[i]
        for (let j = words[i].length; j > 0; j--) {
            tmp = tmp.slice(0, -1)
            if (!words.includes(tmp)) {
                break
            }
        }

        if (tmp === "" && words[i].length >= longest.length) {
            if (words[i].length === longest.length) {
                longest = words[i] < longest ? words[i] : longest;
                continue
            };
            longest = words[i]
        }
    }

    return longest
}

longestWord(input)