from pyscript import display, document

def sample_function(e): 
    # get values from input fields
    name = document.getElementById('text1').value
    age = document.getElementById('text2').value
    school = document.getElementById('text3').value

    # format the output using multiline strings
    message = f"""
    🧑‍🎓 Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

    📝 Notes:
    {name} is currently {age} years old and studies at {school}.
    This information was gathered through input fields and displayed
    using a multiline string in Python via PyScript.
    """

    # show result in the "output" div
    display(message, target="output")