workflow "New workflow" {
  on = "push"
  resolves = ["FormatTest"]
}

action "Build" {
  uses = "actions/docker/cli@76ff57a"
  args = "build -t patrick/code_review_grader ."
}

action "FormatTest" {
  uses = "FormatTest"
  needs = ["Build"]
  runs = "make"
  args = "lint"
}
