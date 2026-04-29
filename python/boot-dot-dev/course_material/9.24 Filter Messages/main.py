# Submitted Solution

def filter_messages(messages):
    msgs_filtered = []
    counts_of_dang = []
    for message in messages:
        good_word_list = []
        dang_counter = 0
        split_message = message.split()
        for i in range(len(split_message)):
            if (split_message[i] == "dang"):
                dang_counter += 1
            else:
                good_word_list.append(split_message[i])
        msgs_filtered.append(" ".join(good_word_list))
        counts_of_dang.append(dang_counter)
    return msgs_filtered, counts_of_dang