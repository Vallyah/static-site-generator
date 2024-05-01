def markdown_to_blocks(markdown):
    block_strings = []
    begin_new_block = True
    current_block_index = -1

    for line in markdown.split("\n"):
        if len(line) == 0:
            begin_new_block = True
        else:
            if begin_new_block:
                current_block_index += 1
                block_strings.append(line)
                begin_new_block = False
            else:
                block_strings[current_block_index] += "\n" + line

    return block_strings
