workflow "New workflow" {
  on = "push"
  resolves = ["PyLint"]
}

action "Build" {
  uses = "actions/docker/cli@76ff57a"
  args = "build -t patrick/code_review_grader ."
}

action "PyLint" {
  uses = "./lint-action"
  needs = ["Build"]
}
