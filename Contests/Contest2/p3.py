class Solution:
    def peopleIndexes(self, favoriteCompanies: list) -> list:
        company_users, results = {}, []
        for user in range(len(favoriteCompanies)):
            company_list = favoriteCompanies[user]
            for company in company_list:
                if company in company_users:
                    company_users[company].append(user)
                else:
                    company_users[company] = [user]
        for user in range(len(favoriteCompanies)):
            company_list = favoriteCompanies[user]
            common_users = set(company_users[company_list[0]])
            common_users.remove(user)
            for company in company_list:
                common_users = common_users & set(company_users[company])

            if len(common_users) == 0:
                results.append(user)
                continue
        return results
