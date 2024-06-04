# Prints a sentence in a centered "box" of correct width
# Note that the integer division operator (//) only works in Python
# 2.2 and newer. In earlier versions, simply use plain division (/)
sentence = input("Sentence: ") # Hello
screen_width = 80
text_width = len(sentence) # text_with = 5
box_width = text_width + 6 # box_with = 11
left_margin = (screen_width - box_width) // 2  # left_margin = 34
print()
print ( ' ' * left_margin + '+' + '-' * (box_width-2) + '+' )
print ( ' ' * left_margin + '| ' + ' ' * (text_width+2) + ' |' )
print ( ' ' * left_margin + '| ' + sentence + ' '*2 +' |' )
print ( ' ' * left_margin + '| ' + ' ' * (text_width+2) + ' |' )
print ( ' ' * left_margin + '+' + '-' * (box_width-2) + '+' )
print()


 #                                 +---------+
  #                                |         |
   #                               | Hello   |
    #                              |         |
     #                             +---------+ 
