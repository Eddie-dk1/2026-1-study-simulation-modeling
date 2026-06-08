
using Test
include(joinpath(@__DIR__, "..", "src", "Lab02.jl"))
using .Lab02

@testset "lab02" begin
    s, i, r = sir_step(0.99, 0.01, 0.0, 0.36, 0.12, 0.5)
    @test isapprox(s + i + r, 1.0; atol = 1e-6)
    x, y = lotka_volterra_step(20.0, 5.0, 1.1, 0.4, 0.1, 0.4, 0.05)
    @test x > 0
    @test y > 0
end
