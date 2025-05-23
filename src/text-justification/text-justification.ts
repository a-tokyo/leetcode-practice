function fullJustify(words: string[], maxWidth: number): string[] {
    const lines: string[] = [];
    let currentWords: string[] = [];
    let currentLen = 0;

    for (let word of words) {
        if (currentLen + currentWords.length + word.length > maxWidth) {
            const totalSpaces = maxWidth - currentLen;
            const gaps = currentWords.length - 1;

            if (gaps === 0) {
                lines.push(currentWords[0] + ' '.repeat(totalSpaces));
            } else {
                const spacePerGap = Math.floor(totalSpaces / gaps);
                let extraSpaces = totalSpaces % gaps;

                let line = '';
                for (let i = 0; i < currentWords.length; i++) {
                    line += currentWords[i];
                    if (i < gaps) {
                        line += ' '.repeat(spacePerGap + (extraSpaces > 0 ? 1 : 0));
                        if (extraSpaces > 0) extraSpaces--;
                    }
                }
                lines.push(line);
            }
            currentWords = [];
            currentLen = 0;
        }

        currentWords.push(word);
        currentLen += word.length;
    }

    const lastLine = currentWords.join(' ');
    lines.push(lastLine + ' '.repeat(maxWidth - lastLine.length));

    return lines;
};