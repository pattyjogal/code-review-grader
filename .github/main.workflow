workflow "New workflow" {
  on = "push"
  resolves = ["FormatTest"]
}

action "Build" {
  uses = "actions/docker/cli@76ff57a"
  args = "build -t patrick/code_review_grader ."
}

action "FormatTest" {
  uses = "actions/bin/filter@b2bea07"
  needs = ["Build"]
  runs = "make"
  args = "lint"
}
