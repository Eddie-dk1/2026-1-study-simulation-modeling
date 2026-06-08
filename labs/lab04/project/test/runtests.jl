
using Test
include(joinpath(@__DIR__, "..", "src", "Lab04.jl"))
using .Lab04

@testset "lab04" begin
    @test infection_probability(0.2, 0) == 0.0
    @test infection_probability(0.2, 2) > 0.2
end
