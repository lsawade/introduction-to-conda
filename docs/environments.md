

## Environment Variables

```bash
echo $PSTYLE
```

```python
from intro2conda.print import customprint

pdict = dict(
    hello=dict(princeton=1, USA=2, world=3), 
    bye=dict(princeton=1, USA=2, world=3))
customprint(pdict)
```

Update `PSTYLE` and run again

```python
from intro2conda.print import customprint

# Make dictionary
pdict = dict(
    hello=dict(princeton=1, USA=2, world=3), 
    bye=dict(princeton=1, USA=2, world=3))

# Print dictionary 2 different ways depending on an environment variable
customprint(pdict)
```

