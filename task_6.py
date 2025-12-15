import json

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_duplicates():
    unique_tickets_dict = {}
    checked_tickets = []
    for key, value in tickets.items():
        for ticket in value:
            if ticket not in checked_tickets:
                if unique_tickets_dict.get(key):
                    unique_tickets_dict[key].append(ticket)
                else:
                    unique_tickets_dict[key] = [ticket]
            checked_tickets.append(ticket)
    return unique_tickets_dict

def merge_tickets(types, tickets):
    tickets_by_type = {}
    for type in types:
        tickets_by_type[types.get(type)] = tickets.get(type)
    tickets_by_type = json.dumps(tickets_by_type, indent=4, ensure_ascii=False)
    return tickets_by_type

unique_tickets_dict = delete_duplicates()
tickets_by_types = merge_tickets(types, unique_tickets_dict)
print(tickets_by_types)