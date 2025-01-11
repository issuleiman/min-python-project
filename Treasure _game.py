road=input("""Welcome to Treasure Island.Your mission is to find the treasure
      You're at a cross road. where do want to go
      Type "left" or "right"  """)


if road=='left':
    island_cross=input("""" you've come to the lake. There is an island in the middle of the lake.
    Type "wait" to wait for the boat. Type "swim" to swim across """)
    if island_cross == 'wait':
        unharmed=input("""" you have arrived unharmed . There are is a house with 3 doors, one red, one yellow , one blue.
                                    choose one of them """)
    else:
        print("Game Over!")

    if unharmed == 'yellow':
        print("you win")
    else:
        print("Game Over!")

else:
    print("Game over!")


