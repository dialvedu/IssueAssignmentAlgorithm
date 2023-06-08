def assign_issues(workers, issues):
    num_workers = len(workers)

    assignment_matrix = [[] for _ in range(num_workers)]
    
    sorted_workers = sorted(range(num_workers), key=lambda x: workers[x][1], reverse=False)
    sorted_issues = sorted(issues, key=lambda x: x[1], reverse=False)
    
    remaining_issues = list(sorted_issues)
    for i, _ in enumerate(remaining_issues):
        issue = remaining_issues[i][0]
        while issue > 0:
            for worker in sorted_workers:
                issues_assigned = min(workers[worker][0], issue)
                assignment_matrix[worker].append((issues_assigned, i))
                issue -= issues_assigned
