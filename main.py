from forum_agents.forum_manager import ForumManager
import time

def main():
    # Initialize forum manager
    forum = ForumManager()
    
    # Create agents with different expertise levels
    agents = [
        forum.create_agent('expert', 5),
        forum.create_agent('expert', 8),
        forum.create_agent('intermediate', 3),
        forum.create_agent('intermediate', 2),
        forum.create_agent('beginner', 1),
        forum.create_agent('beginner', 0)
    ]
    
    # Create initial threads
    threads = {
        'proof_of_work': forum.create_thread(
            'proof_of_work',
            "What are your thoughts on the future of Proof of Work? Should we focus on energy efficiency or security?"
        ),
        'mining_app': forum.create_thread(
            'mining_app',
            "I'm developing a new mobile mining app. What features would you like to see in it?"
        ),
        'future_direction': forum.create_thread(
            'future_direction',
            "Where do you see cryptocurrency mining heading in the next 5 years?"
        )
    }
    
    # Simulate discussions
    for topic, thread_id in threads.items():
        print(f"\nStarting discussion on {topic}...")
        forum.simulate_discussion(thread_id, duration_minutes=15)
        
        # Print thread summary
        summary = forum.get_thread_summary(thread_id)
        print(f"\nThread Summary for {topic}:")
        print(f"Total posts: {summary['post_count']}")
        print(f"Unique participants: {summary['participants']}")
        print(f"Discussion duration: {summary['duration']:.1f} minutes")
        
        # Print all posts in the thread
        print("\nDiscussion:")
        for post in forum.threads[thread_id]:
            print(f"\n{post['username']} ({post['timestamp']}):")
            print(post['content'])
        
        time.sleep(2)  # Brief pause between threads

if __name__ == "__main__":
    main() 