fun square(x: f32): f32, f32 {
    return x, x*x;
}

fun main() {
    let seven = 7;
    let a, b = square(seven);
}