class Fund:
    def __init__(self, code, name, fund_type, one_month, three_months, six_months, from_new_year, one_year, three_years, five_years):
        self.code = code
        self.name = name
        self.fund_type = fund_type
        self.one_month = one_month
        self.three_months = three_months
        self.six_months = six_months
        self.from_new_year = from_new_year
        self.one_year = one_year
        self.three_years = three_years
        self.five_years = five_years

    def as_row(self):
        return '{},{},{},{},{},{},{},{},{},{}\n'.format(
            self.code, self.name, self.fund_type, \
            self.one_month, self.three_months,\
            self.six_months, self.from_new_year,\
            self.one_year, self.three_years, self.five_years)