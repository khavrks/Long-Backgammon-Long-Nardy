import neat
import os
import pickle

from game import Game


def eval_genomes(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        print(round(i/len(genomes) * 100), end=" ")
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[min(i+1, len(genomes) - 1):]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = Game()
            game.play(genome1, genome2, config)

def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-112')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(10))
    winner = p.run(eval_genomes, 100000000)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)
    print("done")


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_file = os.path.join(local_dir, "config.txt")
    print("Loading config")
    config_neat = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    
    run_neat(config_neat)