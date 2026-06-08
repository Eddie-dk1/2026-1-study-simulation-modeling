
using Test
include(joinpath(@__DIR__, "..", "src", "Lab06.jl"))
using .Lab06

@testset "lab06" begin
    s, i, r = petri_sir_step(990, 10, 0, 0.32, 0.11, 1000)
    @test s + i + r == 1000
    @test i >= 0
end
