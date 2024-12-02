def main():
    # import emoji function
    import emoji
    # ask user for a str
    x = input("Input: ").strip()
    # call the emoji function on that string
    print("Output: " + emoji.emojize(x,language='alias'))

main()