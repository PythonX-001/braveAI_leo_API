# Brave Leo

"BraveAI Leo" is a Python module that provides access to Brave's Leo AI chat functionality based on Llama. With this module, you can easily integrate AI chat capabilities powered by Brave's Leo into your Python applications.

## Installation

You can install "braveAI-leo" using pip:

```bash
pip install git+https://github.com/PythonX-001/braveAI_leo_API
```

## Usage

Here's a quick example of how to use "leo_API" to interact with Brave's Leo AI:

Sync,
```python
from leo_API import Leo

# Initialize the Leo instance
leo = Leo()

# Ask to Leo and get a response
response = leo.ask('What is the weather like today?')

print("Leo:", response.completion)
```

Async,
```python
import asyncio
from leo_API import AsyncLeo

async def main():
    # Initialize the Leo instance
    leo = AsyncLeo()

    # Ask to Leo and get a response
    response = await leo.ask('What is the weather like today?')
    print("Leo:", response.completion)

    # Close Session
    await leo.close()

asyncio.run(main())
```

