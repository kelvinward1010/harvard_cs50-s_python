from hello import hello

def main():
    test_default()
    test_argument()
    
def test_default():
    assert hello() == "Hello world"

def test_argument():
    for name in ["Hermione", "Harry"]:
        assert type(hello(name)) == str
        assert hello(name) == f"Hello {name}"

main()
    
# if __name__ == "__main__":
#     main()