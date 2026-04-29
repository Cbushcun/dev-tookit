# Course Assignment Deliverables

> [Lesson Link](https://www.boot.dev/lessons/1d9bbaf7-f597-497d-aebd-4662097ef2f7)

We need to filter the profanity out of our game's live chat feature! Complete the `filter_messages` function. It takes a list of chat messages as input and returns two new lists:

1. A list of the same messages but with all instances of the word `dang` removed.
2. A list containing the number of `dang` words that were removed from each message at that particular index.

Here are some examples:

```
messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]
```

Here are the steps for you to follow. There are a LOT of steps! It won't be easy, but if you follow the steps exactly, you will pass this assignment:

1. Create the two empty lists that you'll return at the end:
   1. One for the filtered messages with "dang" removed.
   2. And one for the counts of "dangs" removed from those messages.
1. Loop over the list of messages. For each message:
   1. Split the message string into a list of words using the .split() string method.
   2. Create an empty list for all the good words in this message.
   3. Create a counter variable for the "dangs" in this message, starting at 0.
   4. For each word in the message:
      1. If the word is "dang", add 1 to the "dangs" counter.
      2. If the word is not "dang", add it to the list of good words.
   5. Join the list of good words into a single string using the .join() method.
   6. Append the new filtered message to the list of filtered messages.
   7. Append the new "dangs" count to the list of counts of "dangs".
1. After looping over the list of messages, return the list of filtered messages first, then the list of "dang" counts.
