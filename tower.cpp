class Tower
{
public:
    std::vector<std::string> towerBuilder(const size_t& nFloors)
    {
        const size_t center = nFloors-1;
        std::string floor (2*nFloors-1, ' ');
        std::vector<std::string> tower;
        for(size_t shift = 0; shift <= center; ++shift)
        {
            floor.replace(center+shift, 1, "*");
            floor.replace(center-shift, 1, "*");
            tower.push_back(floor);
        }
        return tower;
    }
};
