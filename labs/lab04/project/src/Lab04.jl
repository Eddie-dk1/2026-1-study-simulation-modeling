
module Lab04

export infection_probability

infection_probability(beta::Float64, infected_neighbors::Int) = 1 - (1 - beta)^infected_neighbors

end
