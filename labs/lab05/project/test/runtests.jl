
using Test
include(joinpath(@__DIR__, "..", "src", "Lab05.jl"))
using .Lab05

@testset "lab05" begin
    thinking, eating = next_state(5, 0)
    @test thinking == 4
    @test eating == 1
end
