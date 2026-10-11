import streamlit as st
import math

# ==============================================================================
# 1. Core Calculator Functions
# ==============================================================================

def add(a: float, b: float) -> float:
    """Returns the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of a divided by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def modulus(a: float, b: float) -> float:
    """Returns the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot perform modulo by zero!")
    return a % b

def power(a: float, b: float) -> float:
    """Returns a raised to the power of b."""
    return a ** b

def square_root(a: float) -> float:
    """Returns the square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number!")
    return math.sqrt(a)

def percentage(part: float, total: float) -> float:
    """Calculates what percentage part is of total."""
    if total == 0:
        raise ValueError("Total value cannot be zero!")
    return (part / total) * 100

def factorial(n: int) -> int:
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    if not float(n).is_integer():
        raise ValueError("Factorial is only defined for integers!")
    return math.factorial(int(n))

def logarithm(x: float, base: float = 10) -> float:
    """Returns log of x to specified base (default base 10)."""
    if x <= 0:
        raise ValueError("Logarithm argument must be greater than 0!")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1!")
    return math.log(x, base)


# ==============================================================================
# 2. Streamlit Web App Interface
# ==============================================================================

def run_calculator_app():
    try:
        st.set_page_config(
            page_title="Streamlit Calculator",
            page_icon="🧮",
            layout="centered"
        )
    except Exception:
        pass

    st.title("🧮 Comprehensive Calculator App")
    st.write("Perform standard calculations, scientific math, and use an interactive keypad.")

    # Initialize calculation history & keypad state in session state
    if "history" not in st.session_state:
        st.session_state.history = []

    if "expression" not in st.session_state:
        st.session_state.expression = ""

    tab1, tab2, tab3 = st.tabs(["🔢 Standard Calculator", "🔬 Scientific Operations", "📱 Interactive Keypad"])

    # --------------------------------------------------------------------------
    # Tab 1: Standard Calculator
    # --------------------------------------------------------------------------
    with tab1:
        st.subheader("Standard Operations", divider=True)
        
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Enter First Number (A)", value=0.0, format="%f", key="std_num1")
        with col2:
            num2 = st.number_input("Enter Second Number (B)", value=0.0, format="%f", key="std_num2")
            
        operation = st.selectbox(
            "Choose Operation",
            [
                "Addition (+)",
                "Subtraction (-)",
                "Multiplication (×)",
                "Division (÷)",
                "Modulus (%)",
                "Exponent / Power (A^B)"
            ],
            key="std_op"
        )

        if st.button("Calculate", type="primary", key="btn_std_calc", use_container_width=True):
            try:
                if operation == "Addition (+)":
                    res = add(num1, num2)
                    symbol = "+"
                elif operation == "Subtraction (-)":
                    res = subtract(num1, num2)
                    symbol = "-"
                elif operation == "Multiplication (×)":
                    res = multiply(num1, num2)
                    symbol = "×"
                elif operation == "Division (÷)":
                    res = divide(num1, num2)
                    symbol = "÷"
                elif operation == "Modulus (%)":
                    res = modulus(num1, num2)
                    symbol = "%"
                elif operation == "Exponent / Power (A^B)":
                    res = power(num1, num2)
                    symbol = "^"

                result_str = f"{num1} {symbol} {num2} = {res}"
                st.success(f"### Result: **{res}**")
                st.caption(f"Equation: `{result_str}`")
                
                # Save to history
                st.session_state.history.append(result_str)
            except Exception as e:
                st.error(f"Calculation Error: {e}")

    # --------------------------------------------------------------------------
    # Tab 2: Scientific & Special Operations
    # --------------------------------------------------------------------------
    with tab2:
        st.subheader("Single Number & Scientific Operations", divider=True)

        sci_mode = st.radio(
            "Select Function:",
            [
                "Square Root (√x)",
                "Factorial (x!)",
                "Percentage (Part / Total * 100)",
                "Logarithm (log10)",
                "Natural Logarithm (ln)",
                "Trigonometry (sin, cos, tan)"
            ],
            horizontal=True
        )

        if sci_mode == "Square Root (√x)":
            val = st.number_input("Value (x)", value=25.0, key="sci_sqrt")
            if st.button("Calculate Square Root", type="primary", use_container_width=True):
                try:
                    res = square_root(val)
                    item = f"√({val}) = {res}"
                    st.success(f"### Result: **{res}**")
                    st.session_state.history.append(item)
                except Exception as e:
                    st.error(str(e))

        elif sci_mode == "Factorial (x!)":
            val = st.number_input("Integer (n)", value=5, min_value=0, step=1, key="sci_fact")
            if st.button("Calculate Factorial", type="primary", use_container_width=True):
                try:
                    res = factorial(int(val))
                    item = f"{val}! = {res}"
                    st.success(f"### Result: **{res}**")
                    st.session_state.history.append(item)
                except Exception as e:
                    st.error(str(e))

        elif sci_mode == "Percentage (Part / Total * 100)":
            p_part = st.number_input("Part value", value=25.0, key="sci_part")
            p_total = st.number_input("Total value", value=100.0, key="sci_total")
            if st.button("Calculate Percentage", type="primary", use_container_width=True):
                try:
                    res = percentage(p_part, p_total)
                    item = f"({p_part} / {p_total}) * 100 = {res}%"
                    st.success(f"### Result: **{res}%**")
                    st.session_state.history.append(item)
                except Exception as e:
                    st.error(str(e))

        elif sci_mode == "Logarithm (log10)":
            val = st.number_input("Value (x)", value=100.0, min_value=0.0001, key="sci_log")
            if st.button("Calculate log10", type="primary", use_container_width=True):
                try:
                    res = logarithm(val, 10)
                    item = f"log10({val}) = {res}"
                    st.success(f"### Result: **{res}**")
                    st.session_state.history.append(item)
                except Exception as e:
                    st.error(str(e))

        elif sci_mode == "Natural Logarithm (ln)":
            val = st.number_input("Value (x)", value=2.71828, min_value=0.0001, key="sci_ln")
            if st.button("Calculate ln", type="primary", use_container_width=True):
                try:
                    res = math.log(val)
                    item = f"ln({val}) = {res}"
                    st.success(f"### Result: **{res}**")
                    st.session_state.history.append(item)
                except Exception as e:
                    st.error(str(e))

        elif sci_mode == "Trigonometry (sin, cos, tan)":
            angle_deg = st.number_input("Angle in degrees (°)", value=45.0, key="sci_angle")
            rad = math.radians(angle_deg)
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("sin(θ)", f"{math.sin(rad):.4f}")
            with c2:
                st.metric("cos(θ)", f"{math.cos(rad):.4f}")
            with c3:
                try:
                    tan_val = math.tan(rad)
                    st.metric("tan(θ)", f"{tan_val:.4f}")
                except Exception:
                    st.metric("tan(θ)", "Undefined")

    # --------------------------------------------------------------------------
    # Tab 3: Interactive Keypad
    # --------------------------------------------------------------------------
    with tab3:
        st.subheader("Keypad Calculator", divider=True)

        st.text_input("Screen Display", value=st.session_state.expression, key="screen_display", disabled=True)

        def append_expr(char):
            st.session_state.expression += str(char)

        def clear_expr():
            st.session_state.expression = ""

        def eval_expr():
            expr = st.session_state.expression
            if not expr:
                return
            try:
                safe_expr = expr.replace("×", "*").replace("÷", "/")
                allowed_chars = set("0123456789+-*/.() ")
                if not all(ch in allowed_chars for ch in safe_expr):
                    raise ValueError("Invalid characters in expression.")
                
                result = eval(safe_expr)
                record = f"{expr} = {result}"
                st.session_state.expression = str(result)
                st.session_state.history.append(record)
            except Exception:
                st.session_state.expression = "Error"

        # Button Grid (4x5)
        r1 = st.columns(4)
        r1[0].button("C", use_container_width=True, on_click=clear_expr)
        r1[1].button("(", use_container_width=True, on_click=append_expr, args=("(",))
        r1[2].button(")", use_container_width=True, on_click=append_expr, args=(")",))
        r1[3].button("÷", use_container_width=True, on_click=append_expr, args=("÷",))

        r2 = st.columns(4)
        r2[0].button("7", use_container_width=True, on_click=append_expr, args=("7",))
        r2[1].button("8", use_container_width=True, on_click=append_expr, args=("8",))
        r2[2].button("9", use_container_width=True, on_click=append_expr, args=("9",))
        r2[3].button("×", use_container_width=True, on_click=append_expr, args=("×",))

        r3 = st.columns(4)
        r3[0].button("4", use_container_width=True, on_click=append_expr, args=("4",))
        r3[1].button("5", use_container_width=True, on_click=append_expr, args=("5",))
        r3[2].button("6", use_container_width=True, on_click=append_expr, args=("6",))
        r3[3].button("-", use_container_width=True, on_click=append_expr, args=("-",))

        r4 = st.columns(4)
        r4[0].button("1", use_container_width=True, on_click=append_expr, args=("1",))
        r4[1].button("2", use_container_width=True, on_click=append_expr, args=("2",))
        r4[2].button("3", use_container_width=True, on_click=append_expr, args=("3",))
        r4[3].button("+", use_container_width=True, on_click=append_expr, args=("+",))

        r5 = st.columns(4)
        r5[0].button("0", use_container_width=True, on_click=append_expr, args=("0",))
        r5[1].button(".", use_container_width=True, on_click=append_expr, args=(".",))
        r5[2].button("⌫", use_container_width=True, on_click=lambda: setattr(st.session_state, "expression", st.session_state.expression[:-1]))
        r5[3].button("=", use_container_width=True, type="primary", on_click=eval_expr)

    # --------------------------------------------------------------------------
    # Sidebar: Calculation History
    # --------------------------------------------------------------------------
    with st.sidebar:
        st.header("📜 Calculation History")
        if st.button("Clear History", use_container_width=True):
            st.session_state.history = []
            st.rerun()

        if st.session_state.history:
            for idx, item in enumerate(reversed(st.session_state.history), 1):
                st.markdown(f"**{idx}.** `{item}`")
        else:
            st.info("No calculations yet.")


# Execute when run as Streamlit app or standalone script
if __name__ == "__main__":
    run_calculator_app()
