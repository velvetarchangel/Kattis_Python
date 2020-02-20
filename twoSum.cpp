std::pair<std::size_t, std::size_t> two_sum(const std::vector<int>& numbers, int target) {
    int i1 = 0;
    int i2 = 0;
    
    for (int i = 0; i < numbers.size()-1; i++){
      for(int j = i + 1; j < numbers.size(); j ++){
        if (numbers[i] + numbers[j] == target){
          i1 = i;
          i2 = j;
          break;
          }
        }
      }
    return {i1, i2};
}
