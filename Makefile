all:
		sceptre launch-env ${env}

clean:
		rm resolvers/*.pyc

destroy:
		sceptre delete-env ${env}

service-linked-role:
		aws iam create-service-linked-role --aws-service-name ecs.amazonaws.com

execution-role:
		aws iam create-role --role-name ecsTaskExecutionRole --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Sid":","Effect":"Allow","Principal":{"Service":"ecs-tasks.amazonaws.com"},"Action":"sts:AssumeRole"}]}'
		aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonECSTaskExecutionRolePolicy --role-name ecsTaskExecutionRole

.PHONY: clean destroy service-linked-role execution-role
