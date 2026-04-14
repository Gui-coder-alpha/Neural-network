import pygame

def base_floor(screen):
    gray_color = (129, 130, 116)
    floor = (208, 204, 166)

    screen.fill(floor)
    pygame.draw.rect(screen, gray_color, (0, 640, 1280, 720))
    pygame.draw.rect(screen, gray_color, (0, 640, 1280, 750))

def Neural_Hud(screen, best_player, Obstacle):
    red = (255, 0, 0)
    limiar = 0.5
    if best_player != None:
        pos_x = 980
        layer_gap = 90
        node_gap = 40
        node_radius = 15

        Inputs = best_player.neuron.Features(best_player, Obstacle).flatten()
        output_layer, hidden_layer = best_player.neuron.Foward_function(best_player, Obstacle)

        layers = [Inputs, hidden_layer.flatten(), output_layer.flatten()]
        node_position = []

        for neuron_index, layer in enumerate(layers):
            current_layer = []
            nodes_count = max(len(l) for l in layers)
            current_height = len(layer) * node_gap
            network_height = nodes_count * node_gap
            central_networks = (network_height - current_height)/ 2
            for node_index, value in enumerate(layer):
                layer_x = pos_x + neuron_index * layer_gap
                layer_y = central_networks + node_index * node_gap + 40
                current_layer.append((layer_x, layer_y))

                final_color = red if value > limiar else (128, 128, 128)

                pygame.draw.circle(screen, final_color, (layer_x, layer_y), node_radius)
                pygame.draw.circle(screen, (0, 0, 0), (layer_x, layer_y), node_radius, 3)

            node_position.append(current_layer)
        for i in range(len(node_position) - 1):
            for start in node_position[i]:
                for end in node_position[i+1]:
                    pygame.draw.line(screen, (255, 255, 255), start, end, 1)
                    
        for neuron_index, layer in enumerate(layers):
            current_layer = []
            nodes_count = max(len(l) for l in layers)
            current_height = len(layer) * node_gap
            network_height = nodes_count * node_gap
            central_networks = (network_height - current_height)/ 2
            for node_index, value in enumerate(layer):
                layer_x = pos_x + neuron_index * layer_gap
                layer_y = central_networks + node_index * node_gap + 40
                current_layer.append((layer_x, layer_y))

                final_color = red if value > limiar else (128, 128, 128)

                pygame.draw.circle(screen, final_color, (layer_x, layer_y), node_radius)
                pygame.draw.circle(screen, (0, 0, 0), (layer_x, layer_y), node_radius, 3)

            node_position.append(current_layer)