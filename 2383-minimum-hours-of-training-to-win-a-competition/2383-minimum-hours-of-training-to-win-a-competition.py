class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        training_hours = 0
        
        # Energy Check:
        # Total energy needed must be strictly greater than the sum of all opponents' energy.
        total_energy_needed = sum(energy) + 1
        if initialEnergy < total_energy_needed:
            training_hours += total_energy_needed - initialEnergy
            
        # Experience Check:
        # Simulate facing opponents in order and accumulate required experience training.
        current_exp = initialExperience
        for exp in experience:
            if current_exp <= exp:
                # Experience needed to be strictly greater than the opponent's
                diff = exp - current_exp + 1
                training_hours += diff
                current_exp += diff
            # Defeating the opponent grants their experience
            current_exp += exp
            
        return training_hours