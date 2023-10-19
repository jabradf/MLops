Running `pytest` with python debugger, PDB, will allow the program to stop and us to debug it!

```
pytest --pdb test_file.py
```

`h` for help in the console.
`l` to list the error

`string` to see the value of variable `string`

You can manually run commands to see what is happening.

Exit with `c` for continue, or `n` for next.


-----

Other commands we can do:

`pytest -x` : stop after first failure.
`-n 4`: execute tests in parallel. Useful for large test suites as it will split the testing up across threads and CPUs.