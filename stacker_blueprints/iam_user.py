from stacker.blueprints.base import Blueprint

from troposphere import (
    GetAtt,
    Output,
    Ref,
    Sub,
    iam,
)


class IAMUser(Blueprint):
    """
    Blueprint to create an IAM user.

    - class_path: stacker_blueprints.iam_user.IAMUser
      name: my-user
        variables:
          UserName: Bob
          Path: /
    """
    VARIABLES = {
        "UserName": {
            "type": str,
            "description": "List of ARNs of entities allowed to assume this role",
        },
        "Path": {
            "type": str,
            "description": "Provide the path",
            "default": "/",
        },
    }

    def create_template(self):
        user = self.template.add_resource(
            iam.User(**self.get_variables())
        )

        self.template.add_output(
            Output("UserName", Value=Ref(user))
        )

        self.template.add_output(
            Output("UserArn", Value=GetAtt(user, "Arn"))
        )
