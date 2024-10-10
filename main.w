fun square(x: f32): f32, f32 {
    return x, x*x;
}

fun main() {
    let seven = 7;
    let a, b = square(seven);
}

struct Player {
    health: i32;
    mana: i32;

    fun new(): Player {
        Player p;
        p.health = 29;
        p.mana = 3;
        return p;
    }

    fun from(health: i32): Player {
        Player p;
        p.health = health;
        p.mana = 3;
        return p;
    }

    meth damage(amount: i32) {
        this.health -= amount;
    }
}
