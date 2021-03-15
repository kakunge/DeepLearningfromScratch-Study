is_simple_core = False

if is_simple_core:
    from dezero.core_simple import Variable
    from dezero.core_simple import Function
    from dezero.core_simple import using_config
    from dezero.core_simple import no_grad
    from dezero.core_simple import as_array
    from dezero.core_simple import as_variable
    from dezero.core_simple import setup_variable

else:
    from dezero import Variable
    from dezero import Function
    from dezero import using_config
    from dezero import no_grad
    from dezero import as_array
    from dezero import as_variable
    from dezero import setup_variable

setup_variable()