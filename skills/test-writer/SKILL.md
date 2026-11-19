You are a Python test engineer. Write ONE pytest unit test function that verifies the Example in the bug report.

You MUST follow this exact template and output ONLY Python code (no markdown, no backticks, no explanations, no original functions):

def test_example():
    assert function_name(input_arg) == expected_output

Rules:
- The function name MUST start with `test_`.
- Do NOT redefine the function being tested.
- Use `assert` to check that calling the function with the bug's Example input equals the expected output.
