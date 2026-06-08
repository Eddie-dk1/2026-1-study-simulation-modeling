
module Lab02

export sir_step, lotka_volterra_step

function sir_step(s, i, r, beta, gamma, dt)
    ds = -beta * s * i
    di = beta * s * i - gamma * i
    dr = gamma * i
    return s + dt * ds, i + dt * di, r + dt * dr
end

function lotka_volterra_step(x, y, alpha, beta, delta, gamma, dt)
    dx = alpha * x - beta * x * y
    dy = delta * x * y - gamma * y
    return x + dt * dx, y + dt * dy
end

end
