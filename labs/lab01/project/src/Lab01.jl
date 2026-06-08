
module Lab01

export exponential_growth

function exponential_growth(alpha::Float64, t_end::Float64; dt::Float64 = 0.1, u0::Float64 = 1.0)
    n = Int(floor(t_end / dt)) + 1
    t = collect(0.0:dt:t_end)
    u = [u0 * exp(alpha * ti) for ti in t]
    return t, u
end

end
