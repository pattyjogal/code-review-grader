workflow "New workflow" {
  on = "push"
  resolves = ["Build"]
}

action "Build" {
  uses = "actions/docker/cli@76ff57a"
  args = "build -t patrick/code_review_grader ."
}
